from django_assets import Bundle, register

css = Bundle(
    'stylesheets/app.css',
    filters='cssmin',
    output='gen/app.min.css')
register('css_all', css)

js = Bundle(
    'javascripts/foundation/jquery.js',
    # 'javascripts/foundation/jquery.cookie.js',
    # 'javascripts/foundation/jquery.event.move.js',
    # 'javascripts/foundation/jquery.event.swipe.js',
    # 'javascripts/foundation/jquery.foundation.accordion.js',
    # 'javascripts/foundation/jquery.foundation.alerts.js',
    # 'javascripts/foundation/jquery.foundation.buttons.js',
    'javascripts/foundation/jquery.foundation.clearing.js',
    # 'javascripts/foundation/jquery.foundation.forms.js',
    # 'javascripts/foundation/jquery.foundation.joyride.js',
    # 'javascripts/foundation/jquery.foundation.magellan.js',
    'javascripts/foundation/jquery.foundation.mediaQueryToggle.js',
    # 'javascripts/foundation/jquery.foundation.navigation.js',
    # 'javascripts/foundation/jquery.foundation.orbit.js',
    # 'javascripts/foundation/jquery.foundation.reveal.js',
    # 'javascripts/foundation/jquery.foundation.tabs.js',
    # 'javascripts/foundation/jquery.foundation.tooltips.js',
    # 'javascripts/foundation/jquery.foundation.topbar.js',
    # 'javascripts/foundation/jquery.placeholder.js',
    'javascripts/foundation/app.js',
    filters='rjsmin',
    output='gen/app.min.js')

register('js_all', js)
