class PostsController < ApplicationController
    before_action :authenticate_user!, except: [:index, :show]
    def index
     @posts = Post.all
    end

    def new
     @post = current_user.posts.build
    end

    def show
     set_page
    end

    def edit
     set_page
    end

    def update
     set_page
     @post.update(post_params)
     redirect_to @post
    end

    def destroy
     set_page
     @post.destroy
     redirect_to action: "index"
    end



    def create
        @post = current_user.posts.build(post_params)

        respond_to do |format|
            if @post.save
                format.html {redirect_to @post, notice: 'Blog post has been posted!'}
                format.json {render :show, status: :created, location: @post}
            else
                format.html {render :new}
                format.json {render json: @post.errors, status: :unprocessable_entity}
            end   
        end 

    end

    private
    def post_params
        params.require(:post).permit(:title, :content, :header_image, uploads: [])
    end

    def set_page
        @post = Post.friendly.find(params[:id])
    end
end
