Rails.application.routes.draw do
  mount Ckeditor::Engine => '/ckeditor'
  devise_for :users, controllers: { registrations: "registrations"}
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :posts do
    member do
      put "like" => "posts#upvote"
      put "unlike" => "posts#downvote"
    end
  end

  get    '/comments',          to: 'comments#index', as: 'comments'
  post   '/comments',          to: 'comments#create'
  get    '/comments/new',      to: 'comments#new',   as: 'new_comment'
  get    '/comments/:id',      to: 'comments#show',  as: 'comment'
  get    '/comments/:id/edit', to: 'comments#edit',  as: 'edit_comment'
  patch  '/comments/:id',      to: 'comments#update'
  delete '/comments/:id',      to: 'comments#destroy'

  root "posts#index"

  
end
