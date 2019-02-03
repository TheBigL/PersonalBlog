class CreateProjects < ActiveRecord::Migration[5.2]
  def change
    create_table :projects do |t|
      t.integer :project_id
      t.string :weburl
      t.string :githuburl
      t.text :more
      t.boolean :featured

      t.timestamps
    end
  end
end
