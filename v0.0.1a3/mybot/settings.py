from decouple import config

HOSTNAME = ''

PLATFORMS = {
    'telegram': {
        'ENGINE': 'bottery.platform.telegram',
        'OPTIONS': {
            'token': config('TOKEN'),
        }
    },
}
