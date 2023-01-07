from selenium import webdriver

# Read the username and password pairs from the text file
with open('credentials.txt', 'r') as f:
    credentials = [line.strip().split(',') for line in f]

# Create a new Chrome browser
driver = webdriver.Chrome()

# Iterate over the credentials list
for username, password in credentials:
    # Navigate to the Spotify login page
    driver.get('https://accounts.spotify.com/en/login')

    # Find the login form elements
    username_field = driver.find_element_by_id('login-username')
    password_field = driver.find_element_by_id('login-password')
    login_button = driver.find_element_by_id('login-button')

    # Enter the login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)

    # Click the login button
    login_button.click()

    # Search for the artist
    search_field = driver.find_element_by_css_selector('.search-input')
    search_field.send_keys('artist:your-artist-name')
    search_button = driver.find_element_by_css_selector('.search-button')
    search_button.click()

    # Click the first result
    first_result = driver.find_element_by_css_selector('.tracklist-name')
    first_result.click()

    # Find the play button and click it
    play_button = driver.find_element_by_css_selector('.spoticon-play-32')
    play_button.click()
