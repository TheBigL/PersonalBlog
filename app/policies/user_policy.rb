class UserPolicy < ApplicationPolicy

  class Scope < Scope
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized

    attr_reader :current_user, :model

    def initialize(current_user, model)
     @current_user = current_user
     @user = model
    end
   
    def index?
     @current_user.admin?
    end

    def update?
      @current_user.admin?
    end

    def destroy?
      
      if @user = @current_user
        flash[:alert] = "You cannot delete yourself!"
      end

      if @user.admin
        flash[:alert] = "You cannot delete an admin!"
      end
    end

    private
    def user_not_authorized
      flash[:alert] = "You cannot access this part of this site. Admins only!"
    end



  end
end
