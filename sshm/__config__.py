import os
import json
from QuickProject import user_root, user_lang, QproDefaultConsole, QproInfoString, _ask

enable_config = True
config_path = os.path.join(user_root, ".sshm_config")

questions = {
    "path": {
        "type": "input",
        "message": "Default path to save the identity file"
        if user_lang != "zh"
        else "默认保存身份文件的路径",
        "default": os.path.join(user_root, ".ssh"),
    },
}


def init_config():
    with open(config_path, "w") as f:
        json.dump(
            {i: _ask(questions[i]) for i in questions}, f, indent=4, ensure_ascii=False
        )
    QproDefaultConsole.print(
        QproInfoString,
        f'Config file has been created at: "{config_path}"'
        if user_lang != "zh"
        else f'配置文件已创建于: "{config_path}"',
    )


class sshmConfig:
    def __init__(self):
        if not os.path.exists(config_path):
            init_config()
        with open(config_path, "r") as f:
            self.config = json.load(f)

    def select(self, key):
        if key not in self.config and key in questions:
            self.update(key, _ask(questions[key]))
        return self.config.get(key, None)

    def update(self, key, value):
        if value:
            self.config[key] = value
        else:
            self.config.pop(key)
        with open(config_path, "w") as f:
            json.dump(self.config, f, indent=4, ensure_ascii=False)

    def get_all(self):
        res = list(self.config.keys())
        res.remove("path")
        return res
