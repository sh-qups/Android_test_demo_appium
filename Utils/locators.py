

class IntroPageLocator(object):

    add_post = 'com.bikroy:id/intro_post_ad'           # id
    maybe_latter = 'com.bikroy:id/intro_find_ads'           # id
    language = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView'   # xpath

    # location permission popup
    location_permission_all_time = 'com.android.permissioncontroller:id/permission_allow_foreground_only_button'           # id
    location_permission_this_time = 'com.android.permissioncontroller:id/permission_allow_one_time_button'           # id
    location_permission_deny = 'com.android.permissioncontroller:id/permission_deny_button'           # id


class HomePageLocator(object):

    location = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]'     # xpath
    category = 'com.bikroy:id/appbar_category_container'     # id
    filter = 'com.bikroy:id/appbar_filter'     # id
    filter_switch = 'com.bikroy:id/serp_filter_buy_now'     # id

    home = 'com.bikroy:id/main_bottom_panel_home'           # id
    search = 'com.bikroy:id/main_bottom_panel_search'       # id
    add_post_plus_sign = 'com.bikroy:id/btn_post'       # id
    chat = 'com.bikroy:id/main_bottom_panel_chat'           # id
    account = 'com.bikroy:id/main_bottom_panel_my_account'  # id
    first_add = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.viewpager.widget.ViewPager/android.widget.RelativeLayout/android.widget.ImageView'  # xpath


class LocationPageLocator(object):

    user_location = 'com.bikroy:id/location_detection_view'  # id
    search_location = '	com.bikroy:id/search_l2_location'  # id
    all_location = 'com.bikroy:id/location_all_locations'  # id
    dhaka = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'  # xpath
    all_ads_dhaka = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[1]'  # xpath
    back_to_all_locations = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'  # xpath


class CategoryPageLocator(object):

    close_icon = 'com.bikroy:id/filter_activity_close'  # id
    search = 'com.bikroy:id/search_l2_category'  # id
    category_all = 'com.bikroy:id/search_category_all'  # id
    essentials = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'  # xpath
    all_ads_essentials = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[1]'  # xpath
    Mobiles = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]'  # xpath
    all_ads_Mobiles = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[1]'  # xpath
    back_to_all_categories = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.TextView'  # xpath


class FilterPageLocator(object):

    close_icon = 'com.bikroy:id/filter_activity_close'  # id
    sort_by = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.Spinner/android.widget.TextView'  # xpath
    sort_by_low_to_hi = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]'  # xpath
    sort_by_hi_to_low = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[2]'  # xpath
    Type_of_poster = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.Spinner/android.widget.TextView'  # xpath
    all_posters = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[1]'  # xpath
    authorize_dealler = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.TextView[3]'  # xpath
    Filter_by_add = 'com.bikroy:id/chkUrgentFilter'  # id
    clear_all = 'com.bikroy:id/clear_filter'  # id
    apply_filter = 'com.bikroy:id/category_filter_apply'  # id


class SearchPageLocator(object):
    search_main = 'com.bikroy:id/search_verticals'  # id
    search_category_selected = 'com.bikroy:id/edit_search'  # id
    clear_serch = 'com.bikroy:id/home_clear_search'   # id
    popular_search_1 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]'    # xpath
    popular_search_2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]'    # xpath


class ChatsPageLocator(object):
    demo = ''  # id


class AccountPageLocator(object):
    demo = ''  # id


class LoginPageLocator(object):
    gmail = 'com.bikroy:id/sign_in_google_login_button'  # id
    facebook = 'com.bikroy:id/sign_in_facebook_login_button'  # id
    email = 'com.bikroy:id/sign_in_sign_up_email_button'  # id

    email_input = 'com.bikroy:id/sign_in_email'  # id
    password_input = 'com.bikroy:id/sign_in_password'  # id
    login = 'com.bikroy:id/register_register_button'  # id
    forgot_password = 'com.bikroy:id/register_forgot_password'  # id
    # dont_have_account = 'com.bikroy:id/register_have_account_text'  # id
    signup = 'com.bikroy:id/register_signup_button'  # id


class ForgotPasswordPageLocator(object):
    email = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText'  # xpath
    get_me_new_password = 'com.bikroy:id/forgot_password_get_me_password'  # id


class SignupPageLocator(object):
    name_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout/android.widget.EditText'  # xpath
    email_input = 'com.bikroy:id/sign_in_email'  # id
    password_input = 'com.bikroy:id/sign_in_password'  # id
    password_again_input = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.FrameLayout/android.widget.EditText'  # xpath
    signup = 'com.bikroy:id/register_register_button'  # id
    login = 'com.bikroy:id/register_signup_button'  # id
    terms_nd_condition = 'com.bikroy:id/sign_in_terms'   # id
