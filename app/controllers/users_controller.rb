class UsersController < ApplicationController
  before_action :authenticate_user!
  after_action :verify_authorized


# GET /users
# GET /users.json
  def index
    @users = User.all
  end

  # # GET /users/1
# # GET /users/1.json
  def show

  end

  def new
    @user = User.new
  end


  def create
    # Create the user from params
    @user = User.create(user_params)
    if @user.save
      # Deliver the signup email
      UserMailer.registration_confirmation(@user).deliver
      redirect_to(@user, :notice => 'User created')
    else
      render :action => 'new'
    end
  end

# GET /users/1/edit
  def edit

  end

# # PATCH/PUT /users/1
# # PATCH/PUT /users/1.json
  def update
    respond_to do |format|
      if @user.update(user_params)
        format.html { redirect_to @user, notice: 'User was successfully updated.' }
        format.json { render :show, status: :ok, location: @user }
      else
        format.html { render :edit }
        format.json { render json: @user.errors, status: :unprocessable_entity }
      end
    end
  end


  private

  def user_params
    params.require(:user).permit(:username, :email, :password, :password_confirmation)
  end


end
