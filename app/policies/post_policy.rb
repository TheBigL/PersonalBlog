class PostPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      scope.where(user_id: @user.try(:id))
    end
  end

  attr_reader :user, :post

  def initialize(user, record)
    @user = user
    @post = post
  end


  def show?
    true
  end

  def index?
    true
  end

  def create?
    is_contributor_or_admin?
  end

  def update?
    is_author_of_post_or_admin?
  end

  def destroy?
    is_author_of_post_or_admin?
  end



  def is_admin?
    @user.role_id == 1
  end

  def is_contributor_or_admin?
    @user.role_id == 1 || @user.role_id == 2
  end

  private

  def user_not_authorized
    flash[:alert] = "Can't let you do that, " + @user.username + "!"
  end

  def is_author_of_post_or_admin?
    user.username == post.user.username
  end


end
