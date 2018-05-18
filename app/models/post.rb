class Post < ApplicationRecord
 extend FriendlyId
 friendly_id :title, use: :slugged
 belongs_to :user
 acts_as_votable

end
