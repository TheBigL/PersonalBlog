source 'https://rubygems.org'
git_source(:github) { |repo| "https://github.com/#{repo}.git" }

ruby '2.5.1'


# Bundle edge Rails instead: gem 'rails', github: 'rails/rails'
gem 'rails', '~> 5.2.0'
# Use Puma as the app server
gem 'puma', '~> 3.11'
# Use SCSS for stylesheets
gem 'sass-rails', '~> 5.0'
# Use Uglifier as compressor for JavaScript assets
gem 'uglifier', '>= 4.1.20'
# See https://github.com/rails/execjs#readme for more supported runtimes
# gem 'mini_racer', platforms: :ruby

gem "loofah", ">= 2.2.3"



# Use CoffeeScript for .coffee assets and views
gem 'coffee-rails', '~> 4.2'
# Turbolinks makes navigating your web application faster. Read more: https://github.com/turbolinks/turbolinks
gem 'turbolinks', '~> 5.2.0'
# Build JSON APIs with ease. Read more: https://github.com/rails/jbuilder
gem 'jbuilder', '~> 2.5'
# Use Redis adapter to run Action Cable in production
# gem 'redis', '~> 4.0'
# Use ActiveModel has_secure_password
gem 'bcrypt', '~> 3.1.7'

# Use Bulma Rails to simply the CSS part of the site
gem "bulma-rails", "~> 0.7.1"

# Using font-awesome to get icons from font-awesome
gem 'font-awesome-sass', '~> 5.5'


gem "font-awesome-rails"
# Use Simple for Authentication
gem 'simple_form', '~> 4.0.0'

# FriendlyID
gem 'friendly_id', '~> 5.1.0'

# ACME-CLIENT
gem 'acme-client', '~> 2.0', '>= 2.0.1'

gem 'nokogiri', '~> 1.8', '>= 1.8.5'


gem 'sassc', '~> 1.12', '>= 1.12.1'

# Use ActiveStorage variant
gem 'mini_magick', '~> 4.8'

# Use Capistrano for deployment
# gem 'capistrano-rails', group: :development

# Adds likes to comments and blog posts.
gem 'acts_as_votable', '~> 0.11.1'

#Devise - Authnetication Gem
gem 'devise', '~> 4.4', '>= 4.4.3'

#Pundit - Authorization Gem
gem 'pundit', '~> 1.1'




#CKEditor - To make my textarea and blog posts more robust
gem 'ckeditor', '~> 4.2', '>= 4.2.4', github: 'galetahub/ckeditor'

# Reduces boot times through caching; required in config/boot.rb
gem 'bootsnap', '>= 1.1.0', require: false

gem 'carrierwave', '~> 1.0'



group :development, :test do
  # Call 'byebug' anywhere in the code to stop execution and get a debugger console
  gem 'byebug', platforms: [:mri, :mingw, :x64_mingw]

  # Call Rspec to test applications
  gem 'rspec-rails', '~> 3.7'

  #Factory Bot Rails
  gem 'factory_bot_rails', '~> 4.7'


end

group :development do
  # Access an interactive console on exception pages or by calling 'console' anywhere in the code.
  gem 'web-console', '>= 3.3.0'
  gem 'listen', '>= 3.0.5', '< 3.2'
  # Use the better errors gem to better locate stack trace errors.
  gem "better_errors"
  #binding-of-caller
  gem 'binding_of_caller', '~> 0.8.0'
  # Guard is used to simplify running the server
  gem 'guard'
  # Spring speeds up development by keeping your application running in the background. Read more: https://github.com/rails/spring
  gem 'spring'
  gem 'spring-watcher-listen', '~> 2.0.0'
  # Automatically resets the server upon change the view.
  gem 'guard-livereload', '~> 2.5', '>= 2.5.2', require: false

  gem 'rb-readline'

  gem "letter_opener"
end



group :test do
  # Adds support for Capybara system testing and selenium driver
  gem 'capybara', '>= 2.15', '< 4.0'
  gem 'selenium-webdriver'

  #Database Cleaner - Used to clean the database upon finishing a test.
  gem 'database_cleaner'
  # Easy installation and use of chromedriver to run system tests with Chrome
  gem 'chromedriver-helper'
end



# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]

gem 'pg'

# Require bootstrap
gem 'bootstrap', '~> 4.1.1'

#jQuery for Rails!
gem 'jquery-rails', '~> 4.3', '>= 4.3.3'

#Pagination for the site (Note: "kaminari" is Japanese for lightning.)
gem 'kaminari', '~> 1.1', '>= 1.1.1'
