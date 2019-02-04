class AddConfirmables2 < ActiveRecord::Migration[5.2]
  def change
    change_table(:users) do |t|
      t.datetime :confirmed_at
      t.datetime :confirmation_sent_at
      t.string   :unconfirmed_email
    end

    User.update_all confirmed_at: DateTime.now
  end
end
