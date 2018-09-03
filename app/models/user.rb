class User < ApplicationRecord
  enum roles: [:admin, :contributor, :registered, :guest, :banned]
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable
  has_many :posts
  has_many :comments
  has_one_attached :avatar
  before_create :set_default_role



  def set_default_role
     self.role = "registered"
  end

end
