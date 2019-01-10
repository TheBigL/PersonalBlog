class CreateRolesTable < ActiveRecord::Migration[5.2]
  def change
    create_table :roles do |t|
      t.integer :role_id
      t.string :roleName
    end
  end
end
