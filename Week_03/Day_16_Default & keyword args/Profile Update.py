def update_user_profile(existing_profile, **new_info):
    existing_profile.update(new_info)
    return existing_profile

user = {"name": "Ameer Hamza", "GPA": 3.75}
updated_user = update_user_profile(user, GPA=4.0, City="Kohat")
print(updated_user)