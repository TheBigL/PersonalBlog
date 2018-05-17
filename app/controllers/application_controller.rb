class ApplicationController < ActionController::Base
    before_action set_post, except [:index, :new, :create]
    def index
     @posts = Post.all
    end

    def new
     @post = Post.new
    end

    def show
     
    end

    def edit

    end

    def update

     @post.update(post_params)
     redirect_to @post
    end

    def destroy

     @post.destroy
     redirect_to action: "index"
    end



    def create


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

    de

    end    
end
