# 此部分无需修改
SQLALCHEMY_DATABASE_URI = 'sqlite:///cockes.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '111'
JWT_TOKEN_LOCATION = ['headers']
JWT_COOKIE_SECURE = True  # 在开发环境中可以设置为 False，在生产环境中应设置为 True
JWT_COOKIE_CSRF_PROTECT = False
REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 1
REDIS_PASSWORD = None
SHARE_API_URL = "/adminapi/chatgpt/"
CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#以下是需要修改的配置项
#安全配置
SECRET_KEY = '111' # 更换为一个强随机值
SECURITY_PASSWORD_SALT = '123456'  # 更换为一个强随机值
JWT_SECRET_KEY = '123456'  # 更换为一个强随机值
JWT_ACCESS_TOKEN_EXPIRES = 50400  # JWT 访问令牌有效期（单位：秒），例如3600秒（1小时）

#Share配置
SHARE_API_AUTH = "你的api-auth"
SHARE_ADDR = "你的share网址"
