require 'test_helper'
require 'rails_helper'

class UserTest < ActiveSupport::TestCase
  # test "the truth" do
  #   assert true
  # end
  RSpec.describe User, type: :model do


    context "validation tests" do
      it 'ensures Username exists' do
        user = User.new(email: 'test@test.com', password: 'DonkeyKong1981').save()
        expect(user).to eq(false);

      end
    end

  end



end
