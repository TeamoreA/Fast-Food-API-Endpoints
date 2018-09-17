# run.py

'''
Debug the app.
'''
import os
from app import create_app

my_app_config = os.getenv('APP_SETTINGS')
app = create_app(my_app_config)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
