class UserPolicy < ApplicationPolicy
  attr_reader :current_user, :model
  





  class Scope < Scope
    def resolve
      scope
    end
  end
end
