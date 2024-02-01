import hashlib
import logging
from datetime import datetime

# Dictionary to store user credentials and additional information
user_accounts = {}
user_profiles = {}

# Dictionary to store blog posts with categories and timestamps
blog_posts = {}

# Function for user registration (Sign Up)
def register_user(username, password, email=None, age=None):
    if username in user_accounts:
        print("Username already exists. Please choose a different one.")
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        user_accounts[username] = hashed_password
        user_profiles[username] = {'email': email, 'age': age}
        print("Account created successfully. You can now log in.")

# Function for user login (Sign In)
def login_user(username, password):
    if username in user_accounts and user_accounts[username] == hashlib.sha256(password.encode()).hexdigest():
        print(f"Welcome, {username}!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

# Function for posting a blog with categories and timestamps
def post_blog(username, title, content, category='Uncategorized'):
    if username:
        if category not in blog_posts:
            blog_posts[category] = {}
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        blog_posts[category][title] = {'content': content, 'author': username, 'timestamp': timestamp}
        print(f"Blog post '{title}' added successfully to category '{category}' at {timestamp}!")
    else:
        print("You need to log in to post a blog.")

# Function for viewing blogs with categories and timestamps
def view_blogs(category=None):
    if blog_posts:
        if category:
            if category in blog_posts:
                print(f"\n--- {category} Blogs ---")
                for title, details in blog_posts[category].items():
                    print(f"Title: {title}\nContent: {details['content']}\nAuthor: {details['author']}\nTimestamp: {details['timestamp']}\n")
            else:
                print(f"No blogs available in category '{category}'.")
        else:
            print("\n--- All Blogs ---")
            for cat, posts in blog_posts.items():
                for title, details in posts.items():
                    print(f"Category: {cat}\nTitle: {title}\nContent: {details['content']}\nAuthor: {details['author']}\nTimestamp: {details['timestamp']}\n")
    else:
        print("No blog posts available.")

# Additional function for editing a blog post
def edit_blog(username, title, new_content, category='Uncategorized'):
    if username and category in blog_posts and title in blog_posts[category] and blog_posts[category][title]['author'] == username:
        blog_posts[category][title]['content'] = new_content
        print(f"Blog post '{title}' updated successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    else:
        print("You don't have permission to edit this blog or it does not exist.")

# Additional function for deleting a blog post
def delete_blog(username, title, category='Uncategorized'):
    if username and category in blog_posts and title in blog_posts[category] and blog_posts[category][title]['author'] == username:
        del blog_posts[category][title]
        print(f"Blog post '{title}' deleted successfully at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}!")
    else:
        print("You don't have permission to delete this blog or it does not exist.")

# Logging setup
logging.basicConfig(filename='nyka_logs.txt', level=logging.INFO)

print("------- Welcome to Nyka! -------\nWhere you can express yourself\n    within your own space.\n------------------------------\n")
print("~~ Nyka, your safe space ~~\n")

# Main program loop
logged_in_user = None
while True:
    print("1. Sign Up")
    print("2. Sign In")
    print("3. Post a Blog")
    print("4. View Blogs")
    print("5. Edit Blog")
    print("6. Delete Blog")
    print("7. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '1':
        new_username = input("Enter a username: ")
        new_password = input("Enter a password: ")
        new_email = input("Enter your email (optional): ")
        new_age = input("Enter your age (optional): ")
        register_user(new_username, new_password, new_email, new_age)
    elif choice == '2':
        log_username = input("Enter your username: ")
        log_password = input("Enter your password: ")
        logged_in_user = login_user(log_username, log_password)
        if logged_in_user:
            logging.info(f"User '{logged_in_user}' logged in.")
    elif choice == '3':
        if logged_in_user:
            blog_title = input("Enter blog title: ")
            blog_content = input("Enter blog content: ")
            blog_category = input("Enter blog category (optional): ")
            post_blog(logged_in_user, blog_title, blog_content, blog_category)
            logging.info(f"User '{logged_in_user}' posted a blog: '{blog_title}'.")
        else:
            print("You need to log in to post a blog.")
    elif choice == '4':
        view_blogs()
    elif choice == '5':
        if logged_in_user:
            blog_title_to_edit = input("Enter the title of the blog to edit: ")
            new_content = input("Enter the new content for the blog: ")
            blog_category_to_edit = input("Enter the category of the blog (optional): ")
            edit_blog(logged_in_user, blog_title_to_edit, new_content, blog_category_to_edit)
            logging.info(f"User '{logged_in_user}' edited a blog: '{blog_title_to_edit}'.")
        else:
            print("You need to log in to edit a blog.")
    elif choice == '6':
        if logged_in_user:
            blog_title_to_delete = input("Enter the title of the blog to delete: ")
            blog_category_to_delete = input("Enter the category of the blog (optional): ")
            delete_blog(logged_in_user, blog_title_to_delete, blog_category_to_delete)
            logging.info(f"User '{logged_in_user}' deleted a blog: '{blog_title_to_delete}'.")
        else:
            print("You need to log in to delete a blog.")
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, or 7.")
