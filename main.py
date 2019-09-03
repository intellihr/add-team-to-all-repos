import os
from github import Github


token = os.environ['GITHUB_ACCESS_TOKEN']
org_name = os.environ['GITHUB_ORG_NAME']
team_slug = os.environ['GITHUB_TEAM_SLUG']
permission = os.environ['GITHUB_PERMISSION']


g = Github(token)
organistion = g.get_organization(org_name)
team = organistion.get_team_by_slug(team_slug)
repos = organistion.get_repos(sort='full_name')


for repo in repos:
    print('Setting {} access to {}'.format(permission, repo.name))
    team.set_repo_permission(repo, permission)
