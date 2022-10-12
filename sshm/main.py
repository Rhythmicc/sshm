from QuickProject.Commander import Commander
from QuickProject import QproErrorString, is_win
from . import *

app = Commander()


@app.custom_complete("name")
def switch():
    return [
        {
            "name": i,
            "icon": "🔑",
            "description": "Switch to identity file"
            if user_lang != "zh"
            else "切换到身份文件",
        }
        for i in config.get_all()
    ]


@app.command()
def switch(name: str):
    """
    选择一个ssh身份

    :param name: str
    """
    file_dir = config.select(name)
    if not os.path.exists(file_dir):
        QproDefaultConsole.print(
            QproErrorString,
            f'Identity "{name}" does not exist.'
            if user_lang != "zh"
            else f'身份"{name}"不存在.',
        )
        config.update(name, None)
        return
    # 创建软连接
    if is_win:
        external_exec(
            f'cmd /c mklink /D {os.path.join(file_dir, "id_rsa")} {os.path.join(config.select("path"), "id_rsa")}'
        )
        external_exec(
            f'cmd /c mklink /D {os.path.join(file_dir, "id_rsa.pub")} {os.path.join(config.select("path"), "id_rsa.pub")}'
        )
    else:
        external_exec(
            f'ln -snf {os.path.join(file_dir, "id_rsa")} {os.path.join(config.select("path"), "id_rsa")}'
        )
        external_exec(
            f'ln -snf {os.path.join(file_dir, "id_rsa.pub")} {os.path.join(config.select("path"), "id_rsa.pub")}'
        )


@app.command()
def complete():
    """
    自动补全脚本
    """
    from QuickProject.Qpro import gen_complete
    from . import _ask

    if _ask(
        {
            "type": "confirm",
            "message": "此操作将生成complete文件夹, 请确认是否继续"
            if user_lang == "zh"
            else "This operation will generate the complete folder, please confirm whether to continue",
            "default": False,
        }
    ):
        gen_complete("sshm")

        if _ask(
            {
                "type": "confirm",
                "message": "是否应用至全局" if user_lang == "zh" else "Apply to global",
                "default": False,
            }
        ):
            import shutil

            shutil.copy("complete/fig/sshm.ts", "~/.fig/autocomplete/src/sshm.ts")

            shutil.rmtree("complete")


@app.command()
def register(name: str, path: str):
    """
    注册一个ssh身份

    :param name: 身份名称
    :param path: 身份文件夹路径
    """
    if name == "path":
        QproDefaultConsole.print(
            QproErrorString,
            f'Identity name cannot be "path"'
            if user_lang != "zh"
            else f'身份名称不能为"path"',
        )
        return
    from . import _ask

    path = os.path.abspath(path)

    if config.select(name) and not _ask(
        {
            "type": "confirm",
            "message": f'Identity "{name}" already exists, do you want to overwrite it?'
            if user_lang != "zh"
            else f'身份"{name}"已存在, 是否覆盖?',
            "default": False,
        }
    ):
        return

    if not os.path.exists(os.path.join(path, "id_rsa")):
        QproDefaultConsole.print(
            QproErrorString,
            f'Identity file "{os.path.join(path, "id_rsa")}" does not exist.'
            if user_lang != "zh"
            else f'身份文件"{os.path.join(path, "id_rsa")}"不存在.',
        )
        return
    if not os.path.exists(os.path.join(path, "id_rsa.pub")):
        QproDefaultConsole.print(
            QproErrorString,
            f'Identity file "{os.path.join(path, "id_rsa.pub")}" does not exist.'
            if user_lang != "zh"
            else f'身份文件"{os.path.join(path, "id_rsa.pub")}"不存在.',
        )
        return

    config.update(name, path)
    QproDefaultConsole.print(
        QproInfoString,
        f'Identity "{name}" has been registered.'
        if user_lang != "zh"
        else f'身份"{name}"已注册.',
    )


@app.command()
def upgrade():
    """
    升级sshm
    """
    from . import _ask

    if (
        _ask(
            {
                "type": "list",
                "message": "选择升级源" if user_lang == "zh" else "Select upgrade source",
                "choices": ["Github", "Gitee"],
            }
        )
        == "Gitee"
    ):
        external_exec(f"pip3 install git+https://gitee.com/RhythmLian/sshm.git -U")
    else:
        external_exec(f"pip3 install git+https://github.com/Rhythmicc/sshm.git -U")


def main():
    """
    注册为全局命令时, 默认采用main函数作为命令入口, 请勿将此函数用作它途.
    When registering as a global command, default to main function as the command entry, do not use it as another way.
    """
    app()


if __name__ == "__main__":
    main()
