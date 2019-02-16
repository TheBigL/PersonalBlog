class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable, :confirmable
  belongs_to :role
  before_save :setup_role
  after_create :welcome_user



  def setup_role
    if self.username == "LeonardMorrison"
      self.role_id = 1
    else
      self.role_id = 3
    end
  end


  def welcome_user
    UserMailer.account_activation(user).deliver
    redirect_to root_path, alert: "Check your email"

  end











end
