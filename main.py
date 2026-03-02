from pyscript import display, document

def username_verification(e):
    """Check if the username is valid."""
    document.getElementById('output').innerHTML = ''
    username = document.getElementById('username').value.strip()
    
    if len(username) == 0:
        display('❌ You have not filled the Username slot. Please type at least 7 characters.', target='output')
        return False
    elif len(username) < 7:
        display(f'❌ Your username is too short. Add {7 - len(username)} more character(s).', target='output')
        return False
    return True

def password_verification(e):
    """Check if the password is valid."""
    document.getElementById('output').innerHTML = ''
    password = document.getElementById('password').value.strip()
    
    if len(password) == 0:
        display('❌ You have not filled the Password slot. Please type at least 10 characters.', target='output')
        return False
    elif len(password) < 10:
        display(f'❌ Your password is too short. Add {10 - len(password)} more character(s).', target='output')
        return False
    elif not any(char.isalpha() for char in password):
        display('❌ Password must contain at least one letter.', target='output')
        return False
    elif not any(char.isdigit() for char in password):
        display('❌ Password must contain at least one number.', target='output')
        return False
    return True

def account_creation(e):
    """Handle account creation and reveal the Team Picker button."""
    document.getElementById('output').innerHTML = ''
    
    if username_verification(e) and password_verification(e):
        display('✅ Account created! You may now proceed.', target='output')
        document.getElementById('teamBtnContainer').classList.remove('hidden')
    else:
        display('❌ Please correct the errors above and try again.', target='output')