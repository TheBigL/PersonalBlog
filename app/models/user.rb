class User < ApplicationRecord
  # Include default devise modules. Others available are:
  # :confirmable, :lockable, :timeoutable and :omniauthable
  devise :database_authenticatable, :registerable, :recoverable, :rememberable, :trackable, :validatable, :confirmable
  has_many :comments
  belongs_to :role
  has_one_attached :avatar
  before_create :confirmation_token!
  before_save :setup_role
  after_create :welcome_email

  def setup_role
    if self.username == "LeonardMorrison"
      self.role_id = 1
    else
      self.role_id = 3
    end
  end


  private

  def confirmation_token
    if self.confirm_token.blank?
          self.confirm_token = SecureRandom.urlsafe_base64.to_s
      end
  end

  def welcome_email(user)
    UserMailer.registration_confirmation(user)

  end









end
