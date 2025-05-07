# Learning Log

Learning Log is a web app that lets users track topics they’re interested in and write journal entries for each topic. Users can register, log in, and manage their own learning logs.

## Features

- **User Accounts**: Register and log in securely.
- **Topics**: Create topics for areas of interest.
- **Journal Entries**: Add, view, and edit entries for each topic.
- **Homepage**: Describes the site and provides login/registration options.

## How It Works

- **Create a Topic**: Add new topics to organize your learning.
- **Add Entries**: Write journal entries under specific topics.
- **Edit/View Entries**: Review or update your entries as needed.
- **Secure Access**: Only you can view and edit your content after logging in.

## Optional Profile Image in `about_me.html`

If you do **not** plan to include a picture in your `about_me.html` file:

- **Remove** the `{% load static %}` line at the top of the template. This is only needed if you're referencing static files (like images).
- **Remove or replace** the image block:

  ```html
      <div class="text-center pt-2 pb-3">
        <!-- Make sure to replace the picture name and file extension to match your picture
         i.e., 'learning_logs/images/your_picture.jpeg'-->
        <img
        src="{% static 'learning_logs/images/space_red_panda.png' %}"
        alt="Picture of a pastel red panda in a space suit floating in space"
        class="im-fluid rounded-3"
        style="max-width: 130px; height: auto;">
      </div>
