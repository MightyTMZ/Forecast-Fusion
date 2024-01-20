"""
Forecast Fusion: Revolutionizing Weather Forecasting

Uses ESP8266 boards to gather data
Sends the data to the Django server
New snapshot data object is created
The frontend fetches the data periodically (every 15-30 seconds)
We will have a web app, mobile app for users around the world to see their household temperatures
on the frontend interface as numbers, graphs.
|--> we need to make a good authentication and login functionality

Users can log in via web, mobile.
When a user buys a kit, the kit will come with three sensors/pods. Users can also the option of
buying extra pods for their home, but they must register it to their account
As the engineer, you must give each pod a unique code so the user can register them
The code will be put onto the pod upon manufacturing and then immediately put it into our database.

Good luck with this world-changing project!
Remember ideas don't come out fully formed, they only become clearer as you work on them.
You just have to get started!

15-year-old Tom can read an older Tom's mind,
he is thinking about EcoBee and how this project is copying it.

Dear Future Tom,

I hope this letter finds you well and thriving in the world of entrepreneurship.
I'm writing to remind you of something crucial as you venture into building an
IoT app akin to EcoBee. Remember, copying an existing product doesn't guarantee
failure; in fact, it's the unique flavor you bring to the table that can turn it
into something extraordinary.

Right now, at 15, you might be wondering if creating something similar to an
established product is a bold move. Well, it is. But here's why you should
believe in your journey:

Execution is Everything:
Success doesn't always come from reinventing the wheel. It often springs from
how well you execute an idea. Pay attention to the little details, ensure a seamless
user experience, and watch how your dedication shapes the final product.

Learn from the Greats:
Look at EcoBee and other successful products as mentors. Learn from their strengths,
understand their weaknesses, and leverage that knowledge to build something even better.
Seek inspiration without losing sight of your unique perspective.

Innovate Where It Counts:
While your app might share similarities, find innovative ways to implement features, design
interfaces, or integrate additional functionalities. This is where your creative touch can
shine through, making your product stand out.

Your Passion is a Superpower:
Infuse your project with your passion. Make it more than just a venture—it should be an extension
of yourself. When your heart is in it, users can feel the authenticity, making your product more
relatable and compelling.

Continuous Growth is Key:
Stay vigilant to market trends, user feedback, and technological shifts. Adapt, iterate, and always
strive for improvement. The ability to evolve is a defining factor in long-term success.

Building a Legacy, Not Just a Product:
Think beyond the app; focus on building a brand. A positive brand image, effective marketing, and community
engagement can turn your project into a brand people trust and love.

In the journey ahead, remember that success is not a destination but a continuous process of growth and improvement.
Embrace challenges, learn from failures, and celebrate every small victory. And most importantly, don't let your age
define your capabilities. It's a testament to your early entry into a world brimming with possibilities.

Believe in yourself, stay persistent, and let innovation be your guide.

Wishing you the very best,

15-Year-Old ambitious Tom who promised to do good for the world from his kind heart.

"""

from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'forecast_data',
    'product_tracking',
    'users',
    'user_communications', # I did this to not have the users app depend on other apps
    'store'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'forecast_fusion.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'forecast_fusion.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'PORT': os.getenv("DB_PORT"),
        'HOST': os.getenv("DB_HOST"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = "users.CustomUser"

# CORS_ALLOW_ALL_ORIGINS = True

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
}