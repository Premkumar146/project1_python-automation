class Prem_Data:
    username = "Admin"
    password = "admin123"
    firstName= "prem"
    lastName= "kumar"


class Prem_Selectors:
    input_box_username = "username"
    input_box_password = "password"
    login_xpath = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    pim_xpath ='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    addemployee_xpath ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    input_box_firstname ="firstName"
    input_box_lastname ="lastName"
    save_xpath ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'