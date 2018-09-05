class UsersController < ApplicationController
before_filter :authenticate_user!
after_action :verify_authorized

    def show
      @user = User.all
      authorize User
    end

    def destroy
        user = User.find(params[:id])
        authorize user
        @user.destroy

        if @user.destroy
            redirect_to root_url, notice: "The user has been deleted..."
        end

    end

    def update
        @user = User.find(params[:id])
        authorize user
    end


    private
    def set_user
        @user = User.find(params[:id])
    end



end
