class UserPolicy < ApplicationPolicy

  class Scope < Scope
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

    attr_reader :current_user, :model

    def initialize(current_user, model)
     @current_user = current_user
     @user = model
    end

    def show?
      @current_user.role == "admin"?
    end

    def index?
     @current_user.role == "admin"?
    end

    def update?
      @current_user.role == "admin"?
    end

    def destroy?

      user = User.find(params[:id])
      @current_user.role == "admin"?
      if @user = @current_user
        flash[:alert] = "You cannot delete yourself!"
      end

      if @user.admin
        flash[:alert] = "You cannot delete an admin!"
      end
      user.destroy
      redirect_to users_path, :notice => "User has been deleted"


    end

    private
    def user_not_authorized
      flash[:alert] = "You cannot access this part of this site. Only Admins can access this site!"
    end



  end
end
