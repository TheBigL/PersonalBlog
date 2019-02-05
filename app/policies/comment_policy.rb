class CommentPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      scope.where(user_id: @user.try(:id))
    end

    attr_reader :user, :post, :comment

    def initialize(user, comment)
      @user = user
      @post = post
      @comment = comment

    end

    def show?
      true
    end

    def index?
      true
    end

    def create?
      true
    end

    def edit?
      is_author_or_admin?
    end

    def destroy?
      is_author_or_admin?
    end

    private

    def is_admin?
      @user.role_id == 1
    end

    def is_author_or_admin?
      @comment.user.username == @user.username || @user.role_id == 1
    end

    def is_contributor_or_admin?
      @user.role_id == 2 || @user.role_id == 1
    end



  end
end
