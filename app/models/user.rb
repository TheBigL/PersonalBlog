class User < ApplicationRecord
  enum roles: [:admin, :contributor, :registered, :guest, :banned]
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable
  has_many :posts
  has_one_attached :avatar
  
  #before_create :set_default_role
  #belongs_to :role

  roles_attribute :roles_mask
  include RoleModel
  roles: :admin, :contributor, :registered, :guest, :banned
  
  #after_create :assign_default_role

  def set_default_role
     self.role ||= :user
  end
  
end
