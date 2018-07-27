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
      return false if @user.admin? || @current_user = @user
      @current_user.admin?
    end

    private
    def user_not_authorized
      flash[:alert] = "You cannot access this part of this site. Admins only!"
    end



  end
end
