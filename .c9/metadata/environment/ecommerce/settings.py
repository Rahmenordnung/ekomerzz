{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":16,"position":16,"stack":[[{"start":{"row":137,"column":27},"end":{"row":137,"column":28},"action":"insert","lines":["n"],"id":57},{"start":{"row":137,"column":28},"end":{"row":137,"column":29},"action":"insert","lines":["i"]},{"start":{"row":137,"column":29},"end":{"row":137,"column":30},"action":"insert","lines":["e"]},{"start":{"row":137,"column":30},"end":{"row":137,"column":31},"action":"insert","lines":["l"]}],[{"start":{"row":137,"column":31},"end":{"row":137,"column":32},"action":"insert","lines":["s"],"id":58},{"start":{"row":137,"column":32},"end":{"row":137,"column":33},"action":"insert","lines":["-"]}],[{"start":{"row":137,"column":31},"end":{"row":137,"column":32},"action":"remove","lines":["s"],"id":59}],[{"start":{"row":137,"column":28},"end":{"row":137,"column":29},"action":"remove","lines":["i"],"id":60}],[{"start":{"row":137,"column":29},"end":{"row":137,"column":30},"action":"insert","lines":["i"],"id":61}],[{"start":{"row":142,"column":70},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":62}],[{"start":{"row":144,"column":0},"end":{"row":145,"column":0},"action":"insert","lines":["STATICFILES_LOCATION = 'static'",""],"id":63}],[{"start":{"row":144,"column":31},"end":{"row":145,"column":0},"action":"remove","lines":["",""],"id":64}],[{"start":{"row":145,"column":23},"end":{"row":145,"column":63},"action":"remove","lines":["storages.backends.s3boto3.S3Boto3Storage"],"id":65},{"start":{"row":145,"column":23},"end":{"row":145,"column":24},"action":"insert","lines":["c"]},{"start":{"row":145,"column":24},"end":{"row":145,"column":25},"action":"insert","lines":["u"]},{"start":{"row":145,"column":25},"end":{"row":145,"column":26},"action":"insert","lines":["s"]},{"start":{"row":145,"column":26},"end":{"row":145,"column":27},"action":"insert","lines":["t"]},{"start":{"row":145,"column":27},"end":{"row":145,"column":28},"action":"insert","lines":["o"]},{"start":{"row":145,"column":28},"end":{"row":145,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":145,"column":29},"end":{"row":145,"column":30},"action":"insert","lines":["_"],"id":66},{"start":{"row":145,"column":30},"end":{"row":145,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":145,"column":31},"end":{"row":145,"column":32},"action":"insert","lines":["t"],"id":67}],[{"start":{"row":145,"column":32},"end":{"row":145,"column":33},"action":"insert","lines":["o"],"id":68},{"start":{"row":145,"column":33},"end":{"row":145,"column":34},"action":"insert","lines":["r"]},{"start":{"row":145,"column":34},"end":{"row":145,"column":35},"action":"insert","lines":["a"]},{"start":{"row":145,"column":35},"end":{"row":145,"column":36},"action":"insert","lines":["g"]},{"start":{"row":145,"column":36},"end":{"row":145,"column":37},"action":"insert","lines":["e"]},{"start":{"row":145,"column":37},"end":{"row":145,"column":38},"action":"insert","lines":["s"]}],[{"start":{"row":145,"column":38},"end":{"row":145,"column":39},"action":"insert","lines":["."],"id":69},{"start":{"row":145,"column":39},"end":{"row":145,"column":40},"action":"insert","lines":["S"]},{"start":{"row":145,"column":40},"end":{"row":145,"column":41},"action":"insert","lines":["t"]},{"start":{"row":145,"column":41},"end":{"row":145,"column":42},"action":"insert","lines":["a"]},{"start":{"row":145,"column":42},"end":{"row":145,"column":43},"action":"insert","lines":["t"]},{"start":{"row":145,"column":43},"end":{"row":145,"column":44},"action":"insert","lines":["i"]}],[{"start":{"row":145,"column":44},"end":{"row":145,"column":45},"action":"insert","lines":["c"],"id":70},{"start":{"row":145,"column":45},"end":{"row":145,"column":46},"action":"insert","lines":["S"]},{"start":{"row":145,"column":46},"end":{"row":145,"column":47},"action":"insert","lines":["t"]}],[{"start":{"row":144,"column":0},"end":{"row":150,"column":1},"action":"remove","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticSt'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")"],"id":76},{"start":{"row":144,"column":0},"end":{"row":153,"column":53},"action":"insert","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'","","STATIC_URL = '/static/'","STATICFILES_DIRS = (","    os.path.join(BASE_DIR, \"static\"),",")","","MEDIAFILES_LOCATION = 'media'","DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'"]}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":2},"action":"insert","lines":["# "],"id":77}],[{"start":{"row":82,"column":0},"end":{"row":89,"column":78},"action":"remove","lines":["# DATABASES = {","#     'default': {","#         'ENGINE': 'django.db.backends.sqlite3',","#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","#     }","# }","","DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}"],"id":78},{"start":{"row":82,"column":0},"end":{"row":91,"column":5},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"]}]]},"ace":{"folds":[],"scrolltop":1069,"scrollleft":0,"selection":{"start":{"row":90,"column":9},"end":{"row":90,"column":9},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":70,"state":"start","mode":"ace/mode/python"}},"timestamp":1565127150678,"hash":"db4824df99886fd115bc30e08b7bca511ca98b18"}