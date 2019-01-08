class RemoveCommentIDfromComments < ActiveRecord::Migration[5.2]
  def change
    remove_column :comments, :comment_id, :integer
    remove_index :comments, :post_id
  end
end
