class CommentPolicy < ApplicationPolicy
  class Scope < Scope
    def resolve
      scope.where(user_id: @user.try(:id))
    end


    
  end
end
