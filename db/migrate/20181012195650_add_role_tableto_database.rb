class AddRoleTabletoDatabase < ActiveRecord::Migration[5.2]
  def change
    create_table :roles do |t|
      t.integer :roleId
      t.string :roleName
    end
    remove_column :users, :role
  end
end