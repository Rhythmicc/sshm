const completionSpec: Fig.Spec = {
    "name": "sshm",
    "description": "sshm",
    "subcommands": [
        {
            "name": "--help",
            "description": "获取帮助",
            "options": [
                {
                    "name": "--hidden",
                    "description": "显示隐藏命令"
                }
            ]
        },
        {
            "name": "complete",
            "description": "获取补全列表",
            "args": [],
            "options": [
                {
                    "name": "--team",
                    "description": "团队名",
                    "isOptional": true,
                    "args": {
                        "name": "team",
                        "description": "团队名"
                    }
                },
                {
                    "name": "--token",
                    "description": "团队token",
                    "isOptional": true,
                    "args": {
                        "name": "token",
                        "description": "团队token"
                    }
                },
                {
                    "name": "--is_script",
                    "description": "是否为脚本"
                }
            ]
        },
        {
            "name": "switch",
            "description": "选择一个ssh身份",
            "args": [
                {
                    "name": "name",
                    "description": "str",
                    "suggestions": [
                        {
                            "name": "rhythmlian",
                            "icon": "🔑",
                            "description": "切换到身份文件"
                        },
                        {
                            "name": "sugon",
                            "icon": "🔑",
                            "description": "切换到身份文件"
                        },
                        {
                            "name": "weifengliu",
                            "icon": "🔑",
                            "description": "切换到身份文件"
                        }
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "register",
            "description": "注册一个ssh身份",
            "args": [
                {
                    "name": "name",
                    "description": "身份名称"
                },
                {
                    "name": "path",
                    "description": "身份文件夹路径",
                    "template": [
                        "filepaths",
                        "folders"
                    ]
                }
            ],
            "options": []
        },
        {
            "name": "upgrade",
            "description": "升级sshm",
            "args": [],
            "options": []
        }
    ]
};
export default completionSpec;
