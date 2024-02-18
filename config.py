SQLALCHEMY_DATABASE_URI = 'sqlite:///cockes.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = '' # secret_key:api加密
SECURITY_PASSWORD_SALT = ''  # 更换为一个强随机值

# Redis 配置
REDIS_HOST = ''
REDIS_PORT = 6380
REDIS_DB = 0
REDIS_PASSWORD = None

# JWT 配置
JWT_SECRET_KEY = '333'  # 更换为一个强随机值
JWT_ACCESS_TOKEN_EXPIRES = 50400  # JWT 访问令牌有效期（单位：秒），例如3600秒（1小时）
JWT_TOKEN_LOCATION = ['headers']
JWT_COOKIE_SECURE = False  # 在开发环境中可以设置为 False，在生产环境中应设置为 True
JWT_COOKIE_CSRF_PROTECT = False

# Share 配置
SHARE_API_URL = "/adminapi/chatgpt/"
SHARE_ADDR = ""
SHARE_API_AUTH = ""
FREE_TIME = 36500  # 免费时间设置为100年
PLUS_WHEN_REGISTER_TIME = 0  # PLUS的使用时间，单位为天, 默认为0

CHAR_SET = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
