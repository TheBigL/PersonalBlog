FactoryBot.define do
  factory :project do
    project_id { 1 }
    weburl { "MyString" }
    string { "MyString" }
    github { "" }
    featured { false }
  end
end
