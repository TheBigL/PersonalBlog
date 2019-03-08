Rails.application.routes.draw do
  mount Ckeditor::Engine => '/ckeditor'
  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts do
    resources :comments
  end
  resources :projects
  get 'static/aboutme'
  get 'static/aboutmejp'



  root "posts#index"
  get '/check.txt', to: proc { [200, {}, ['it_works']] }


end
