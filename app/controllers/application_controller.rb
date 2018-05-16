class ApplicationController < ActionController::Base
    
    def index
     @posts = Post.all
    end

    def new
     @post = Post.new
    end

    def show
     @post = Post.friendly.find(params[:id])
    end

    def edit
     @post = Post.friendly.find(params[:id])
    end

    def update
     @post = Post.friendly.find(params[:id])
     @post.update(post_params)
     redirect_to @post
    end

    def destroy
     @post = Post.friendly.find(params[:id])
     @post.destroy
     redirect_to action: "index"
    end



    def create
        @post = Post.new(post_params)

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
        params.require(:post).permit(:title, :content)
    end
end
