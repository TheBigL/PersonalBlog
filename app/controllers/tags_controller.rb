class TagsController < ApplicationController
  before_action :set_tag, only: %i[show edit update destroy]
  before_action :authentication_required!, except: %i[index show]
end
