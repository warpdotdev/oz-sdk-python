# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import agent
from .. import _compat
from .scope import Scope as Scope
from .factory import Factory as Factory
from .harness import Harness as Harness
from .error_code import ErrorCode as ErrorCode
from .secret_ref import SecretRef as SecretRef
from .agent_skill import AgentSkill as AgentSkill
from .environment import Environment as Environment
from .user_profile import UserProfile as UserProfile
from .harness_param import HarnessParam as HarnessParam
from .agent_run_params import AgentRunParams as AgentRunParams
from .memory_store_ref import MemoryStoreRef as MemoryStoreRef
from .secret_ref_param import SecretRefParam as SecretRefParam
from .agent_list_params import AgentListParams as AgentListParams
from .mcp_server_config import McpServerConfig as McpServerConfig
from .agent_run_response import AgentRunResponse as AgentRunResponse
from .environment_config import EnvironmentConfig as EnvironmentConfig
from .agent_list_response import AgentListResponse as AgentListResponse
from .aws_provider_config import AwsProviderConfig as AwsProviderConfig
from .factory_list_params import FactoryListParams as FactoryListParams
from .gcp_provider_config import GcpProviderConfig as GcpProviderConfig
from .harness_auth_secrets import HarnessAuthSecrets as HarnessAuthSecrets
from .agent_config_snapshot import AgentConfigSnapshot as AgentConfigSnapshot
from .memory_store_ref_param import MemoryStoreRefParam as MemoryStoreRefParam
from .session_sharing_config import SessionSharingConfig as SessionSharingConfig
from .mcp_server_config_param import McpServerConfigParam as McpServerConfigParam
from .agent_list_models_response import AgentListModelsResponse as AgentListModelsResponse
from .harness_auth_secrets_param import HarnessAuthSecretsParam as HarnessAuthSecretsParam
from .inference_providers_config import InferenceProvidersConfig as InferenceProvidersConfig
from .agent_config_snapshot_param import AgentConfigSnapshotParam as AgentConfigSnapshotParam
from .agent_get_artifact_response import AgentGetArtifactResponse as AgentGetArtifactResponse
from .session_sharing_config_param import SessionSharingConfigParam as SessionSharingConfigParam
from .aws_inference_provider_config import AwsInferenceProviderConfig as AwsInferenceProviderConfig
from .agent_list_environments_params import AgentListEnvironmentsParams as AgentListEnvironmentsParams
from .agent_list_environments_response import AgentListEnvironmentsResponse as AgentListEnvironmentsResponse
from .inference_providers_config_param import InferenceProvidersConfigParam as InferenceProvidersConfigParam
from .aws_inference_provider_config_param import AwsInferenceProviderConfigParam as AwsInferenceProviderConfigParam
from .networking_get_egress_ranges_response import (
    NetworkingGetEgressRangesResponse as NetworkingGetEgressRangesResponse,
)
from .agent_get_run_by_external_reference_params import (
    AgentGetRunByExternalReferenceParams as AgentGetRunByExternalReferenceParams,
)
from .agent_get_run_by_external_reference_response import (
    AgentGetRunByExternalReferenceResponse as AgentGetRunByExternalReferenceResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    agent.conversation_step.ConversationStep.update_forward_refs()  # type: ignore
    agent.run_get_conversation_response.RunGetConversationResponse.update_forward_refs()  # type: ignore
    agent.conversation_retrieve_response.ConversationRetrieveResponse.update_forward_refs()  # type: ignore
else:
    agent.conversation_step.ConversationStep.model_rebuild(_parent_namespace_depth=0)
    agent.run_get_conversation_response.RunGetConversationResponse.model_rebuild(_parent_namespace_depth=0)
    agent.conversation_retrieve_response.ConversationRetrieveResponse.model_rebuild(_parent_namespace_depth=0)
