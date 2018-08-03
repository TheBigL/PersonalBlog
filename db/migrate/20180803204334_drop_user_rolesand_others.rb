class DropUserRolesandOthers < ActiveRecord::Migration[5.2]
  #Remember this for when you want to remove items from a schema.
  def change
    drop_table :users_roles
    remove_column :users, :role_id, :integer
  end
end
