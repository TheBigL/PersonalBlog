class Post < ApplicationRecord
 extend FriendlyId
 friendly_id :title, use: :slugged
 acts_as_votable
 belongs_to :user
 has_one_attached :header_image
 has_one_attached :upload
 has_many :comments
 paginates_per 10
 max_paginates_per 25
end
