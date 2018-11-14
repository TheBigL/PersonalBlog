class PostPolicy < ApplicationPolicy





  class PolicyScope < Scope
    include Pundit
    rescue_from Pundit::NotAuthorizedError, with: :user_not_authorized


    attr_reader :user, :record

    def initialize_user(current_user, record)
      @user = current_user
      @post = record
    end

    def resolve
      if @user.role_id == 1
        scope.all
      end
    end

  end

  def show?
    true
  end

  def index?
    true
  end

  def create?
    @user.role_id == 1? && record.user == @user?
  end

  def update?
    @user.present? && @user.role_id == 1? || @user.role_id == 2?
  end

  def destroy?
    @user.present? && @user.role_id == 1? || @post.user_id == @user.user_id?
  end

  private

  def user_not_authorized
    flash[:alert] = "Can't let you do that, " + @user.username + "!"
  end

end
