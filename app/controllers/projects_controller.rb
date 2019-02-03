class ProjectsController < ApplicationController
  before_action :authenticate_user!, except: [:index, :show]

  after_action :verify_authorized, except: [:index, :show]

  def index
   @projects = Project.order(created_at: :desc).page(params[:page]).per(10)
  end

  def show
    set_project
  end

  def new
    @project = Project.build
    authorize @project
  end

  def update
    authorize @project
    respond_to do |format|
      if @project.update(project_params)
        format.html { redirect_to @project, notice: 'Project was successfully updated.' }
        format.json { render :show, status: :ok, location: @project }
      else
        format.html { render :edit }
        format.json { render json: @project.errors, status: :unprocessable_entity }
      end
    end
  end


  def destroy
    authorize @project
    set_project

    @project.destroy
    respond_to do |format|
      format.html { redirect_to projects_url, notice: 'Project was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private

  # Use callbacks to share common setup or constraints between actions.
  def set_project
    @project = Project.find_by_slug(params[:id])
  end

  # Never trust parameters from the scary internet, only allow the white list through.
  def project_params
    params.require(:project).permit(:title, :description, :weburl, :giturl, :more, :featured, :image)
  end
end
