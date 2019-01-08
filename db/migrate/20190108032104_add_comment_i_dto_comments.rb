class AddCommentIDtoComments < ActiveRecord::Migration[5.2]
  def change
    add_column :comments, :comment_id, :integer
    add_index :comments, :post_id
  end
end
