from os import system

scrape=__import__('scrape')
class_data=__import__('read_class_data').get_data()

allow=True
while allow:

    roll=input("Enter Roll No/Type in 'quit' for exiting:\n").strip()
    if roll=='quit':
        allow=False
        continue

    else:
        if roll in class_data:
            print("Reading Profile...\n")
            user_personal=class_data[roll]
            profile=scrape.read_codechef_profile(user_personal['handle'])
            print('Name:',user_personal['name'])
            if profile==None:
                print('Incorrect Handle found:',user_personal['handle'],"!")
            else:
                print('Stars:',profile['stars'])
                print('Current Rating:',profile['current_rating'])
                print('Global Rank:',profile['global_rank'])
                print('Country Rank:',profile['country_rank'])
                print('No. of contests participated in:',len(profile['work']),'\n(From Jan,2018 to Present)')
                if len(profile['work'])!=0:
                    print('Contest wise Data:')
                    for i in profile['work']:
                        print(i,profile['work'][i])
        else:
            print('Roll Number not found!')

        print('-----------------------------------------------------')