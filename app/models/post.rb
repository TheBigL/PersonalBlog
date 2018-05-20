class Post < ApplicationRecord
 extend FriendlyId
 friendly_id :title, use: :slugged
 acts_as_votable
 belongs_to :user
end
