class RemoveIdonRole < ActiveRecord::Migration[5.2]
  def change
    remove_column :id, :roles
  end
end
